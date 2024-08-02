package api.crazy.demo.domain.entities;

public class Example {
    
	public String id;
	public String name;


	public Example(){
	}

	public Example(String id,String name){
		this.id = id;
		this.name = name;
	}

	public void setId(String id){
		this.id = id;
	}

	public String getId(String id){
		return this.id;
	}

	public void setName(String name){
		this.name = name;
	}

	public String getName(String name){
		return this.name;
	}




    @Override
    public String toString() {
        return 	"{" +
			"\"id\": \"" + id + "\"," + 
			"\"name\": \"" + name +
		"}";
    }
    

}
