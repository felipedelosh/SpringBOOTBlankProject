//WANING: this code is autogenerated with GCA by FelipedelosH
package api.crazy.demo.infraestructure.DAO.UserDAO;

import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import jakarta.persistence.Column;
import lombok.AllArgsConstructor;
import lombok.NoArgsConstructor;
import lombok.Builder;
import lombok.Data;

@Entity
@Table(name = "<DATABASE-TABLE-NAME>")
@AllArgsConstructor
@NoArgsConstructor
@Builder
@Data
public class UserEntity {

	@Id
	@Column(name = "id")
	public String id;

	@Column(name = "username")
	public String username;

	@Column(name = "contrasena")
	public String contrasena;

	@Column(name = "name")
	public String name;

	@Column(name = "age")
	public int age;



}