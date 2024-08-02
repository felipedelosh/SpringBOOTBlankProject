package api.crazy.demo.infraestructure.DAO.OrderDAO;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

public interface OrderRepository extends JpaRepository<OrderEntity, String> {

    @Query(
            value = "select * from <TABLE-DB-ENTITY>",
            nativeQuery = true
    )
    List<OrderEntity> getAll();
    
}
