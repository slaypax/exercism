import java.util.Map;
import java.util.HashMap;

class RnaTranscription {

    String transcribe(String dnaStrand) {
        String rnaTranscription = "";
        HashMap<Character, Character> nucleotides = new HashMap<>() {
            {
            put('G','C');
            put('C','G');
            put('T','A');
            put('A','U');
            }
        };
        for (int i = 0; i < dnaStrand.length(); i++) {
            rnaTranscription += nucleotides.get(dnaStrand.charAt(i));
        }
        return rnaTranscription;
    }
}
