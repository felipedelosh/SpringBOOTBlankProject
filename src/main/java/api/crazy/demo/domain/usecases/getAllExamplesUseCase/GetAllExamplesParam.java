package api.crazy.demo.domain.usecases.getAllExamplesUseCase;

public class GetAllExamplesParam {

    private GetAllExamplesParam(){
    }

    //This is static becos not need instance... with put static you utilized without instance.
    //Only used a method
    public static GetAllExamplesParam build(){
        return new GetAllExamplesParam();
    }
    
}
