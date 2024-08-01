package api.crazy.demo.infraestructure.entryPoints;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

//Dependencias para "Inyectar caso de uso"
import api.crazy.demo.domain.usecases.getAllExamplesUseCase.GetAllExamplesUseCase;
import api.crazy.demo.domain.usecases.getAllExamplesUseCase.GetAllExamplesParam;


@RestController
public class getExamplesApiRest {

    private final GetAllExamplesUseCase getAllExamplesUseCase;

    public getExamplesApiRest(GetAllExamplesUseCase getAllExamplesUseCase){
        this.getAllExamplesUseCase = getAllExamplesUseCase;
    }

    @GetMapping("/getExamples")
	public String index() {

        var response = getAllExamplesUseCase.call(GetAllExamplesParam.build());

		return response.toString();
	}

}
