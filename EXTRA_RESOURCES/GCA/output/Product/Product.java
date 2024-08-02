package api.crazy.demo.domain.entities;

public class Product {
    
	public String id;
	public String name;
	public Double price;


	public Product(){
	}

	public Product(String id,String name,Double price){
		this.id = id;
		this.name = name;
		this.price = price;
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

	public void setPrice(Double price){
		this.price = price;
	}

	public Double getPrice(Double price){
		return this.price;
	}




    @Override
    public String toString() {
        return 	"{" +
	"\"id\": \"" + id + "\"," + 
	"\"name\": \"" + name + "\"," + 
	"\"price\": \"" + price +
	"}";
    }
    

}
