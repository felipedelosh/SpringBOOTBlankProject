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

	public String getId(String id){
		return this.id;
	}

	public void setUserId(String userId){
		this.userId = userId;
	}

	public String getUserId(String userId){
		return this.userId;
	}

	public void setStatus(String status){
		this.status = status;
	}

	public String getStatus(String status){
		return this.status;
	}




    @Override
    public String toString() {
        return 	"{" +
	"\"id\": \"" + id + "\"," + 
	"\"userId\": \"" + userId + "\"," + 
	"\"status\": \"" + status +
	"}";
    }
    

}
