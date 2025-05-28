<template>
    <span class="circular-dial">
        <svg width="120" height="120" viewBox="0 0 200 200">
            <text
                x="100"
                y="105" text-anchor="middle"
                dominant-baseline="middle"
                font-family="sans-serif"
                font-size="40" font-weight="bold"
                fill="grey"
                opacity="0.8" >
                {{ title }}
            </text>
            <path :d="greenArc" fill="green" stroke="none" />
            <path :d="amberArcClockwise" fill="orange" stroke="none" stroke-width="25" />
            <path :d="amberArcCounterClockwise" fill="orange" stroke="none" stroke-width="25" />
            <path :d="redArcClockwise" fill="red" stroke="none" stroke-width="25" />
            <path :d="redArcCounterClockwise" fill="red" stroke="none" stroke-width="25" />

            <path d="M 0 -80 L -4 -15 L 0 0 L 4 -15 Z" fill="currentColor" stroke="black" stroke-width="2" :transform="needleTransform" />
        </svg>

        <p>Current {{ title }}: {{ currentCondition !== null ? currentCondition.toFixed(1) : 'N/A' }}</p>
        <p>lower limit: {{ greenLowLimit.toFixed(1) }}</p>
        <p>upper limit: {{ greenUpLimit.toFixed(1) }}</p>
        
    </span>
</template>

<script>
export default {
    props: {
        greenLowerLimit: {
            type: Number,
            required: true,
        },
        greenUpperLimit: {
            type: Number,
            required: true,
        },
        zoneDegrees: {
            type: Array,
            required: false,
        },
        currentCondition: {
            type: Number,
            required: false,
            default: null
        },
        title: {
            type: String,
            required: true,
            validator: function (value) {
                // Optional: Ensure only valid titles are passed
                return ['VPD', 'CO²', '°C'].includes(value);
            }
        }
    },
    computed: {
        unitsPerDegree() {
            const unitsPerDegree = (this.greenUpperLimit - this.greenLowerLimit) / this.sumZoneDegrees;
            return unitsPerDegree;
        },
        sumZoneDegrees() {
            return this.zoneDegrees.reduce((sum, val) => sum + val, 0);
        },
        greenLowLimit() {
            return this.greenLowerLimit;
        },
        greenUpLimit() {
            return this.greenUpperLimit;
        },
        amberLowerLimit() {
            const amberZone = this.unitsPerDegree * this.zoneDegrees[1];
            return this.greenLowerLimit - amberZone;
        },
        amberUpperLimit() {
            const amberZone = this.unitsPerDegree * this.zoneDegrees[1];
            return this.greenUpperLimit + amberZone;
        },
        redLowerLimit() {
            const redZone = this.unitsPerDegree * this.zoneDegrees[2];
            return this.amberLowerLimit - redZone;
        },
        redUpperLimit() {
            const redZone = this.unitsPerDegree * this.zoneDegrees[2];
            return this.amberUpperLimit + redZone;
        },
        baseArc() {
            const centerX = 100;
            const centerY = 100;
            const radius = 80;
            const startAngle = -150;
            const endAngle = 150;
            return this.describeArc(centerX, centerY, radius, startAngle, endAngle);
        },
        greenArc() {
            const centerX = 100;
            const centerY = 100;
            const radiusOuter = 80;
            const radiusInner = 80 - 25;
            const startAngle = -this.zoneDegrees[0] / 2;
            const endAngle = this.zoneDegrees[0] / 2;
            return this.describeFilledArc(centerX, centerY, radiusOuter, radiusInner, startAngle, endAngle);
        },
        amberArcClockwise() {
            const centerX = 100;
            const centerY = 100;
            const radiusOuter = 80;
            const radiusInner = 80 - 25;
            const startAngle = this.zoneDegrees[0] / 2;
            const endAngle = startAngle + this.zoneDegrees[1];
            return this.describeFilledArc(centerX, centerY, radiusOuter, radiusInner, startAngle, endAngle);
        },
        amberArcCounterClockwise() {
            const centerX = 100;
            const centerY = 100;
            const radiusOuter = 80;
            const radiusInner = 80 - 25;
            const startAngle = -this.zoneDegrees[0] / 2;
            const endAngle = startAngle - this.zoneDegrees[1];
            return this.describeFilledArc(centerX, centerY, radiusOuter, radiusInner, startAngle, endAngle, true);
        },
        redArcClockwise() {
            const centerX = 100;
            const centerY = 100;
            const radiusOuter = 80;
            const radiusInner = 80 - 25;
            const startAngle = this.zoneDegrees[0] / 2 + this.zoneDegrees[1];
            const endAngle = startAngle + this.zoneDegrees[2];
            return this.describeFilledArc(centerX, centerY, radiusOuter, radiusInner, startAngle, endAngle);
        },
        redArcCounterClockwise() {
            const centerX = 100;
            const centerY = 100;
            const radiusOuter = 80;
            const radiusInner = 80 - 25;
            const startAngle = -this.zoneDegrees[0] / 2 - this.zoneDegrees[1];
            const endAngle = startAngle - this.zoneDegrees[2];
            return this.describeFilledArc(centerX, centerY, radiusOuter, radiusInner, startAngle, endAngle, true);
        },
        needleTransform() {
            const rotation = this.calculateNeedleRotation();
            return `translate(100, 100) rotate(${rotation}) translate(0, 15)`;
        },
    },
    methods: {
        polarToCartesian(centerX, centerY, radius, angleInDegrees) {
            const angleInRadians = (angleInDegrees - 90) * Math.PI / 180.0;
            return {
                x: centerX + (radius * Math.cos(angleInRadians)),
                y: centerY + (radius * Math.sin(angleInRadians))
            };
        },
        describeArc(x, y, radius, startAngle, endAngle) {
            const start = this.polarToCartesian(x, y, radius, endAngle);
            const end = this.polarToCartesian(x, y, radius, startAngle);
            const largeArcFlag = endAngle - startAngle <= 180 ? "0" : "1";
            const d = [
                "M", start.x, start.y,
                "A", radius, radius, 0, largeArcFlag, 0, end.x, end.y
            ].join(" ");
            return d;
        },
        describeFilledArc(centerX, centerY, radiusOuter, radiusInner, startAngle, endAngle, isCounterClockwise = false) {
            let startOuter, endOuter, startInner, endInner;
            const largeArcFlag = Math.abs(endAngle - startAngle) <= 180 ? "0" : "1";
            const outerSweepFlag = !isCounterClockwise ? "1" : "0"; // Clockwise: 1, Counter-Clockwise: 0
            const innerSweepFlag = !isCounterClockwise ? "0" : "1"; // Clockwise: 0, Counter-Clockwise: 1

            if (isCounterClockwise) {
                startOuter = this.polarToCartesian(centerX, centerY, radiusOuter, startAngle);
                endOuter = this.polarToCartesian(centerX, centerY, radiusOuter, endAngle);
                startInner = this.polarToCartesian(centerX, centerY, radiusInner, startAngle);
                endInner = this.polarToCartesian(centerX, centerY, radiusInner, endAngle);
            } else {
                // Correcting the order of startAngle and endAngle for clockwise
                startOuter = this.polarToCartesian(centerX, centerY, radiusOuter, startAngle);
                endOuter = this.polarToCartesian(centerX, centerY, radiusOuter, endAngle);
                startInner = this.polarToCartesian(centerX, centerY, radiusInner, startAngle);
                endInner = this.polarToCartesian(centerX, centerY, radiusInner, endAngle);
            }

            const d = [
                "M", startOuter.x, startOuter.y,
                "A", radiusOuter, radiusOuter, 0, largeArcFlag, outerSweepFlag, endOuter.x, endOuter.y,
                "L", endInner.x, endInner.y,
                "A", radiusInner, radiusInner, 0, largeArcFlag, innerSweepFlag, startInner.x, startInner.y,
                "Z"
            ].join(" ");
            return d;
        },
        calculateNeedleRotation() {
            const lowerLimit = this.greenLowerLimit;
            const upperLimit = this.greenUpperLimit;
            const current = this.currentCondition;
            const greenDegrees = this.zoneDegrees[0];
            

            // Map the current value to the green zone range (-greenDegrees/2 to greenDegrees/2)
            const percentage = (current - lowerLimit) / (upperLimit - lowerLimit);
            const rotation = (percentage-0.5) * greenDegrees; // Subtract 0.5 to center around 12 o'clock
            

            return rotation;
        },
    }
}
</script>

<style scoped>
.circular-dial {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.circular-dial p {
    font-size: 0.5em; /* Adjusted font size for better readability */
    margin: 5px 0;
}
</style>
