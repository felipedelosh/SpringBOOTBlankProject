package api.crazy.demo.infraestructure.entryPoints;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

//Dependencias para "Inyectar caso de uso"
import api.crazy.demo.domain.usecases.getAllUserUseCase.GetAllUserUseCase;
import api.crazy.demo.domain.usecases.getAllUserUseCase.GetAllUserUseCaseParam;


@RestController
public class getUserApiRest {

    private final GetAllUserUseCase getalluserusecase;

    public getExamplesApiRest(GetAllUserUseCase getalluserusecase){
        this.getalluserusecase = getalluserusecase;
    }

    @GetMapping("/getAllUser")
	public String index() {

        var response = getalluserusecase.call(GetAllUserUseCaseParam.build());

		return response.toString();
	}

}
