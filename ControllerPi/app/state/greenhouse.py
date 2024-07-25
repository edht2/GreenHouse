from app.main.bed import Bed
from app.main.climz import ClimateZone
from app.controll.solenoid import Solenoid
from app.controll.acctuator import Acctuator

# climateZone1
bed1 = Bed(Solenoid(33), 1, 1)
bed2 = Bed(Solenoid(34), 2, 1)
bed3 = Bed(Solenoid(35), 3, 1)
bed4 = Bed(Solenoid(36), 4, 1)
bed5 = Bed(Solenoid(37), 5, 1)
bed6 = Bed(Solenoid(38), 6, 1)
heating_solenoid = Solenoid(39)
misting_solenoid = Solenoid(40)

window_side1 = Acctuator([14, 13], 60)
window_side2 = Acctuator([16, 15], 60)
window_side3 = Acctuator([18, 17], 60)
window_side4 = Acctuator([20, 19], 60)
window_side5 = Acctuator([22, 21], 60)
window_top1 = Acctuator([24, 23], 60)
window_top2 = Acctuator([26, 24], 60)
window_top3 = Acctuator([28, 27], 60)
window_top4 = Acctuator([30, 19], 60)
window_top5 = Acctuator([32, 31], 60)
cz1 = ClimateZone(
    beds=[bed1, bed2, bed3, bed4, bed5, bed6],
    top_windows=[window_top1, window_top2, window_top3, window_top4, window_top5],
    side_windows=[window_side1, window_side2, window_side3, window_side4, window_side5],
    heating_solenoid=heating_solenoid,
    misting_solenoid=misting_solenoid,
    climateZoneNumber=1)

# climateZone2
bed6 = Bed(Solenoid(41), 1, 2)
bed7 = Bed(Solenoid(42), 2, 2)
bed8 = Bed(Solenoid(43), 3, 2)
heating_solenoid = Solenoid(44)
misting_solenoid = Solenoid(45)

window_side1 = Acctuator([2, 1], 60)
window_side2 = Acctuator([4, 3], 60)
window_side3 = Acctuator([6, 5], 60)
window_top1 = Acctuator([8, 7], 60)
window_top2 = Acctuator([10, 9], 60)
window_top3 = Acctuator([12, 11], 60)
cz2 = ClimateZone(
    beds=[bed6, bed7, bed8],
    top_windows=[window_top1, window_top2, window_top3],
    side_windows=[window_side1, window_side2],
    heating_solenoid=heating_solenoid,
    misting_solenoid=misting_solenoid,
    climateZoneNumber=2)

czs = [cz1, cz2]
