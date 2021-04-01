import java.util.Arrays;


class ResistorColorDuo {
    int value(String[] colors) {
        String resistorCode = String.format("%s%s", colorCode(colors[0]), colorCode(colors[1]));
        return Integer.parseInt(resistorCode);
    }

    int colorCode(String color) {
        return Arrays.asList(colors()).indexOf(color);
    }

    String[] colors() {
        return new String[] {"black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"};
    }
}
