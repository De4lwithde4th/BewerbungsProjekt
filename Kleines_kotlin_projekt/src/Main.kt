// 1️⃣ Klasse definieren
class Konto(var kontostand: Double) {
    private val buchungen = mutableListOf<String>()

    fun einzahlen(betrag: Double) {
        kontostand += betrag
        buchungen.add("+$betrag€ eingezahlt")
    }

    fun abheben(betrag: Double) {
        if (betrag <= kontostand) {
            kontostand -= betrag
            buchungen.add("-$betrag€ abgehoben")
        } else {
            println("Nicht genug Guthaben!")
        }
    }

    fun kontoauszug() {
        println("Kontostand: $kontostand€")
        println("Letzte Buchungen:")
        buchungen.takeLast(5).forEach { println(it) }
    }
}

fun kontoStand(konto: Konto){
    konto.kontoauszug()
}

fun geldEinzahlen(konto: Konto){
    println("Betrag zum einzahlen: ")
    val betrag = readln().toDoubleOrNull()
    if (betrag != null && betrag > 0){
        konto.einzahlen(betrag)
    }else{
        println("Ungültige eingabe")
    }
}

fun geldAbheben(konto: Konto){
    println("Betrag zum abheben angeben: ")
    val betrag = readln().toDoubleOrNull()
    if(betrag != null && betrag > 0){
        konto.abheben(betrag)
    }else{
        println("Ungültige eingabe")
    }
}

fun pinAbfrage(): Boolean {
    val korrekterPin = "1234"
    var versuche = 3

    while (versuche > 0) {
        println("Bitte Pin eingeben")
        val eingabe = readln()

        if (eingabe == korrekterPin) {
            println("Pin ist Korrekt")
            return true
        } else {
            versuche--
            println("Falsche pin noch $versuche übrig")
        }
    }

    println("zuviele versuche zugriff gesperrt")
    return false
}

fun main(){
    if(!pinAbfrage()){
        return
    }
    val konto = Konto(1000.0)

    while (true){
        println("\n1), Einzahlen 2), Abheben 3), kontoAuszug 4) Beenden")
        println("Auswählen")
        when(readln()){
            "1" -> geldEinzahlen(konto)
            "2" -> geldAbheben(konto)
            "3" -> kontoStand(konto)
            "4" -> {
                println("Programm geschlossen")
                return
            }
            else -> println("Ungültige eingabe")
        }
    }
}


