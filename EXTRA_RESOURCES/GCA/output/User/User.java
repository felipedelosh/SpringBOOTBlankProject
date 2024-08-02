package api.crazy.demo.domain.entities;

public class User {
    
	public String id;
	public String username;
	public String contrasena;
	public String name;
	public int age;


	public User(){
	}

	public User(String id,String username,String contrasena,String name,int age){
		this.id = id;
		this.username = username;
		this.contrasena = contrasena;
		this.name = name;
		this.age = age;
	}

	public void setId(String id){
		this.id = id;
	}

	public String getId(String id){
		return this.id;
	}

	public void setUsername(String username){
		this.username = username;
	}

	public String getUsername(String username){
		return this.username;
	}

	public void setContrasena(String contrasena){
		this.contrasena = contrasena;
	}

	public String getContrasena(String contrasena){
		return this.contrasena;
	}

	public void setName(String name){
		this.name = name;
	}

	public String getName(String name){
		return this.name;
	}

	public void setAge(int age){
		this.age = age;
	}

	public int getAge(int age){
		return this.age;
	}




    @Override
    public String toString() {
        return 	"{" +
			"\"id\": \"" + id + "\"," + 
			"\"username\": \"" + username + "\"," + 
			"\"contrasena\": \"" + contrasena + "\"," + 
			"\"name\": \"" + name + "\"," + 
			"\"age\":"  + age +
		"}";
    }
    

}
