package api.crazy.demo.infraestructure.DAO.ExampleDAO;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

public interface ExampleRepository extends JpaRepository<ExampleEntity, String> {

    @Query(
            value = "select * from examples",
            nativeQuery = true
    )
    List<ExampleEntity> getAll();
    
}
