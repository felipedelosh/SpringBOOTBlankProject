//WANING: this code is autogenerated with GCA by FelipedelosH
package api.crazy.demo.domain.entities;

public class Order {
    
	public String id;
	public String userId;
	public String status;


	public Order(){
	}

	public Order(String id,String userId,String status){
		this.id = id;
		this.userId = userId;
		this.status = status;
	}

	public void setId(String id){
		this.id = id;
	}

	public String getId(){
		return this.id;
	}

	public void setUserId(String userId){
		this.userId = userId;
	}

	public String getUserId(){
		return this.userId;
	}

	public void setStatus(String status){
		this.status = status;
	}

	public String getStatus(){
		return this.status;
	}




    @Override
    public String toString() {
        return 	"{" +
			"\"id\": \"" + id + "\"," + 
			"\"userId\": \"" + userId + "\"," + 
			"\"status\": \"" + status + "\"" + 
		"}";
    }
    

}
