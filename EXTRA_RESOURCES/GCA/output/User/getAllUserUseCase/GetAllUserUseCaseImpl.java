package api.crazy.demo.domain.usecases.getAllUserUseCase;

import java.util.List;
import java.util.ArrayList;
import org.springframework.stereotype.Component;

import api.crazy.demo.domain.entities.User;
import api.crazy.demo.infraestructure.DAO.UserDAO.UserEntity;
import api.crazy.demo.infraestructure.DAO.UserDAO.UserService;
//Convert database info in Java Class
import api.crazy.demo.infraestructure.mappers.UserMapper;

@Component //This decorator permit injection
public class GetAllUserUseCaseImpl extends GetAllUserUseCase {

    private final UserService userservice;

    public GetAllExamplesUseCaseImpl(UserService userservice){
        this.userservice = userservice;
    }

    @Override
    public List<User> call(GetAlluserserviceParam param) {

        List<User> x = new ArrayList<>();
        List<<ENTITYENTITY>> y = userservice.getAll();

        for (int i = 0; i < y.size(); i++) {
            x.add(UserMapper.toDomain(y.get(i)));
        }

        return x;
    }

}
