package api.crazy.demo.domain.entities;

public class Example {
    
    public String id;
    public String name;

    public Example() {
    }

    public Example(String id, String name) {
        this.id = id;
        this.name = name;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    @Override
    public String toString() {
        return "Example{" +
                "id='" + id + '\'' +
                ", name='" + name + '\'' +
                '}';
    }

}
