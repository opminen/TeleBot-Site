package api.rest.entety;

public class CardEntety {

    public static Integer count = -1;
    public Integer id;
    private String name;
    private String text;

    public CardEntety() { count++; this.id = count; }
    public CardEntety(String name, String text) {
        count++;
        this.id = count;
        this.name = name;
        this.text = text;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }
}
