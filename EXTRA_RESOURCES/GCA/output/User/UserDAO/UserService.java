package api.crazy.demo.infraestructure.DAO.UserDAO;

import java.util.List;
import org.springframework.stereotype.Service;

import lombok.AllArgsConstructor;

@Service
@AllArgsConstructor
public class UserService {

    private final UserRepository userrepository;

    public List<UserEntity> getAll(){
        var x = userrepository.findAll();
        return x;
    }
    
}
