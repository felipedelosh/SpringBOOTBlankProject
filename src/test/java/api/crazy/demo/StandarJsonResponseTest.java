package api.crazy.demo;

import api.crazy.demo.domain.entities.StandarJsonResponse;

import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;
import static org.junit.jupiter.api.Assertions.*;


@SpringBootTest
public class StandarJsonResponseTest {


    @Test
	void getResponseTrueWithData() {

        StandarJsonResponse resp = new StandarJsonResponse();
        resp.setStatus(true);
        resp.setData("[]");
        resp.setCode("200");

    
        assertNotNull(resp);
        assertNotNull(resp.toString());
        assertEquals(resp.isStatus(), true);
        assertNotEquals(resp.getData(), null);
    }
    
}
