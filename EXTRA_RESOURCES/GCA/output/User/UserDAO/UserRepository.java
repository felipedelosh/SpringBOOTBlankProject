package api.crazy.demo.infraestructure.DAO.UserDAO;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

public interface UserRepository extends JpaRepository<UserEntity, String> {

    @Query(
            value = "select * from <TABLE-DB-ENTITY>",
            nativeQuery = true
    )
    List<UserEntity> getAll();
    
}
