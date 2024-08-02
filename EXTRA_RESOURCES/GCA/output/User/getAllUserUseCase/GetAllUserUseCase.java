package api.crazy.demo.domain.usecases.getAllUserUseCase;

import java.util.List;
import api.crazy.demo.domain.entities.User;

public abstract class GetAllUserUseCase {
    
    public abstract List<User> call(GetAllUserParam param);

}