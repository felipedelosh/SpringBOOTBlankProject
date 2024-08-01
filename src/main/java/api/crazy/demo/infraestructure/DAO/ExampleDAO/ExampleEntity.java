package api.crazy.demo.infraestructure.DAO.ExampleDAO;

import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import jakarta.persistence.Column;
import lombok.AllArgsConstructor;
import lombok.NoArgsConstructor;
import lombok.Builder;
import lombok.Data;

@Entity
@Table(name = "examples")
@AllArgsConstructor
@NoArgsConstructor
@Builder
@Data
public class ExampleEntity {

    @Id
    @Column(name = "id")
    private String id;
    
    @Column(name = "name")
    private String name;

}