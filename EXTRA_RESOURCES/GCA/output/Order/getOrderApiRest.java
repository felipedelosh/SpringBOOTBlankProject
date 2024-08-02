package api.crazy.demo.infraestructure.entryPoints;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

//Dependencias para "Inyectar caso de uso"
import api.crazy.demo.domain.usecases.getAllOrderUseCase.GetAllOrderUseCase;
import api.crazy.demo.domain.usecases.getAllOrderUseCase.GetAllOrderUseCaseParam;


@RestController
public class getOrderApiRest {

    private final GetAllOrderUseCase getallorderusecase;

    public getExamplesApiRest(GetAllOrderUseCase getallorderusecase){
        this.getallorderusecase = getallorderusecase;
    }

    @GetMapping("/getAllOrder")
	public String index() {

        var response = getallorderusecase.call(GetAllOrderUseCaseParam.build());

		return response.toString();
	}

}
