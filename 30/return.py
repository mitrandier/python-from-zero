def convert_seconds(seconds):
    hours= seconds // 3600
    minoutes = ((seconds -  hours * 3600 ) // 60)
    remaining_seconds = ( seconds -  hours * 3600  -  minoutes * 60 )
    return hours, remaining_seconds, minoutes

hours,minutes,seconds = convert_seconds(5000)
print(hours, minutes, seconds)
