package api.crazy.demo.infraestructure.DAO.ProductDAO;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

public interface ProductRepository extends JpaRepository<ProductEntity, String> {

    @Query(
            value = "select * from <TABLE-DB-ENTITY>",
            nativeQuery = true
    )
    List<ProductEntity> getAll();
    
}
