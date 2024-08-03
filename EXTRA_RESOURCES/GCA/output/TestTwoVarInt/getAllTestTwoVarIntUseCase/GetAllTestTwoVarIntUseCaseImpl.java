//WANING: this code is autogenerated with GCA by FelipedelosH
package api.crazy.demo.domain.usecases.getAllTestTwoVarIntUseCase;

import java.util.List;
import java.util.ArrayList;
import org.springframework.stereotype.Component;

import api.crazy.demo.domain.entities.TestTwoVarInt;
import api.crazy.demo.infraestructure.DAO.TestTwoVarIntDAO.TestTwoVarIntEntity;
import api.crazy.demo.infraestructure.DAO.TestTwoVarIntDAO.TestTwoVarIntService;
//Convert database info in Java Class
import api.crazy.demo.infraestructure.mappers.TestTwoVarIntMapper;

@Component //This decorator permit injection
public class GetAllTestTwoVarIntUseCaseImpl extends GetAllTestTwoVarIntUseCase {

    private final TestTwoVarIntService testtwovarintservice;

    public GetAllTestTwoVarIntUseCaseImpl(TestTwoVarIntService testtwovarintservice){
        this.testtwovarintservice = testtwovarintservice;
    }

    @Override
    public List<TestTwoVarInt> call(GetAllTestTwoVarIntUseCaseParam param) {

        List<TestTwoVarInt> x = new ArrayList<>();
        List<TestTwoVarIntEntity> y = testtwovarintservice.getAll();

        for (int i = 0; i < y.size(); i++) {
            x.add(TestTwoVarIntMapper.toDomain(y.get(i)));
        }

        return x;
    }

}
