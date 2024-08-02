package api.crazy.demo.infraestructure.entryPoints;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

//Dependencias para "Inyectar caso de uso"
import api.crazy.demo.domain.usecases.getAllProductUseCase.GetAllProductUseCase;
import api.crazy.demo.domain.usecases.getAllProductUseCase.GetAllProductUseCaseParam;


@RestController
public class getProductApiRest {

    private final GetAllProductUseCase getallproductusecase;

    public getExamplesApiRest(GetAllProductUseCase getallproductusecase){
        this.getallproductusecase = getallproductusecase;
    }

    @GetMapping("/getAllProduct")
	public String index() {

        var response = getallproductusecase.call(GetAllProductUseCaseParam.build());

		return response.toString();
	}

}
