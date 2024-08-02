package api.crazy.demo.infraestructure.entryPoints;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

//Dependencias para "Inyectar caso de uso"
import api.crazy.demo.domain.usecases.getAllExampleUseCase.GetAllExampleUseCase;
import api.crazy.demo.domain.usecases.getAllExampleUseCase.GetAllExampleUseCaseParam;


@RestController
public class getExampleApiRest {

    private final GetAllExampleUseCase getallexampleusecase;

    public getExamplesApiRest(GetAllExampleUseCase getallexampleusecase){
        this.getallexampleusecase = getallexampleusecase;
    }

    @GetMapping("/getAllExample")
	public String index() {

        var response = getallexampleusecase.call(GetAllExampleUseCaseParam.build());

		return response.toString();
	}

}
