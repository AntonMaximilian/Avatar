import asyncio
import edge_tts

DOCTOR_VOICE = "de-DE-AmalaNeural"
PATIENT_VOICE = "de-DE-ConradNeural"

dialog = [
    # 0 - Begrüßung
    ("doctor", "Guten Tag! Ich freue mich, dass Ihre Operation gut verlaufen ist. Ich möchte Ihnen nun ein paar wichtige Dinge erklären, damit Sie wissen, was Sie in den nächsten Tagen und Wochen beachten sollten. Haben Sie kurz Zeit?"),
    ("patient", "Ja natürlich, vielen Dank! Ich bin froh, dass alles gut gelaufen ist."),

    # 1 - Ablauf der nächsten Tage
    ("doctor", "Sehr gut. Dann fangen wir an mit dem Ablauf der nächsten Tage. Morgen früh um sieben Uhr gibt es eine kurze ärztliche Visite. Dabei wird Ihr Fall an das Folgeteam übergeben. Mittags findet dann eine ausführliche Visite statt, bei der alles in Ruhe besprochen wird."),
    ("patient", "Okay, also morgens erstmal die Übergabe und mittags dann ausführlich. Soll ich mir Fragen aufschreiben?"),
    ("doctor", "Genau, das ist eine super Idee! Notieren Sie sich tagsüber gerne alle Fragen, die Ihnen einfallen. Bei der Mittagsvisite können wir dann alles in Ruhe durchgehen."),

    # 2 - Wundversorgung
    ("doctor", "Jetzt zur Wundversorgung. Ihre Wunde wurde geklebt. Das Pflaster, das sich auf der Wunde befindet, können Sie nach drei Tagen vorsichtig entfernen. Wichtig ist, dass Sie die Wunde trocken und sauber halten. Bitte nicht daran kratzen oder reiben."),
    ("patient", "Verstanden. Also Pflaster nach drei Tagen ab und die Wunde in Ruhe lassen."),

    # 3 - Fäden ziehen
    ("doctor", "Falls bei Ihnen Fäden verwendet wurden, sollten diese nach vierzehn Tagen gezogen werden. Dafür können Sie entweder zu Ihrem Hausarzt gehen, oder Sie kommen einfach zu uns in die Klinik. Sie können sich jederzeit ohne Termin zwischen neun und elf Uhr bei uns vorstellen."),
    ("patient", "Ah das ist ja praktisch, dass ich auch ohne Termin vorbeikommen kann. Also zwischen neun und elf Uhr, richtig?"),
    ("doctor", "Genau, einfach zwischen neun und elf vorbeikommen, ganz unkompliziert."),

    # 4 - Duschen & Baden
    ("doctor", "Zum Thema Duschen und Baden: Sie dürfen bereits nach drei Tagen wieder duschen. Lassen Sie das Wasser kurz über die Wunde laufen, aber reiben Sie bitte nicht daran. Baden, Schwimmen und Saunagänge sollten Sie für mindestens vier Wochen vermeiden."),
    ("patient", "Also Duschen nach drei Tagen ist okay, aber kein Baden oder Schwimmen für vier Wochen."),

    # 5 - Bewegung
    ("doctor", "Genau. Und was Bewegung angeht: Leichte Spaziergänge sind von Anfang an erwünscht und helfen sogar bei der Heilung. Vermeiden Sie aber schweres Heben über fünf Kilogramm für die nächsten sechs Wochen. Und wechseln Sie regelmäßig Ihre Position — also nicht zu lange am Stück sitzen oder stehen."),
    ("patient", "Okay, also spazieren gehen ist gut, aber nichts Schweres heben. Und immer mal die Position wechseln."),

    # 6 - Schmerzmittel
    ("doctor", "Richtig. Zu Ihrer Schmerzmedikation: Nehmen Sie die verordneten Schmerzmittel ruhig nach Bedarf ein. Bitte halten Sie Schmerzen nicht einfach aus, sondern nehmen Sie rechtzeitig Ihre Medikamente. Sollten die Schmerzen trotz Medikation zunehmen, kontaktieren Sie bitte Ihren Arzt."),
    ("patient", "Gut zu wissen. Also lieber rechtzeitig nehmen und nicht erst warten bis es schlimm wird."),

    # 7 - Warnsignale
    ("doctor", "Genau. Und jetzt noch etwas Wichtiges: Bitte achten Sie auf bestimmte Warnsignale. Kontaktieren Sie sofort einen Arzt bei Fieber über achtunddreißig Komma fünf Grad, bei zunehmender Rötung, Schwellung oder Eiter an der Wunde, bei neu auftretenden Taubheitsgefühlen oder Lähmungen in den Beinen, bei Problemen beim Wasserlassen oder Stuhlgang, oder bei starken zunehmenden Schmerzen trotz Medikation."),
    ("patient", "Okay, also bei Fieber, Rötung, Taubheit oder wenn irgendetwas komisch ist, sofort melden."),
    ("doctor", "Genau, lieber einmal zu viel anrufen als einmal zu wenig."),

    # 8 - Abschluss
    ("doctor", "Zum Abschluss: Bitte nehmen Sie Ihren vereinbarten Kontrolltermin wahr. Falls eine Rehabilitation geplant ist, erhalten Sie die Unterlagen von uns. Und bei Fragen können Sie sich jederzeit an uns wenden. Ich wünsche Ihnen eine gute und schnelle Genesung!"),
    ("patient", "Vielen herzlichen Dank für die ausführliche Erklärung! Dann weiß ich ja jetzt gut Bescheid."),
]

async def generate():
    for i, (speaker, text) in enumerate(dialog):
        voice = DOCTOR_VOICE if speaker == "doctor" else PATIENT_VOICE
        filename = f"audio/{i:02d}_{speaker}.mp3"
        print(f"Generating {filename}...")
        communicate = edge_tts.Communicate(text, voice, rate="-5%")
        await communicate.save(filename)
    print("Done!")

asyncio.run(generate())
