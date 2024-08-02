package api.crazy.demo.infraestructure.DAO.OrderDAO;

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
public class OrderEntity {

	@Id
	@Column(name = "id")
	public String id;

	@Column(name = "userId")
	public String userId;

	@Column(name = "status")
	public String status;



}