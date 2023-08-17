package api.rest.controller;

import api.rest.entety.CardEntety;
import org.springframework.web.bind.annotation.*;

import java.util.HashMap;
import java.util.Map;

@RestController
@RequestMapping("/card")
@CrossOrigin
public class CardController {

    private Map<Integer, CardEntety> db = new HashMap<Integer, CardEntety>();

    @GetMapping("{id}")
    public CardEntety getCard(@PathVariable Integer id) {
        return db.get(id);
    }

    @GetMapping("/")
    public Map<Integer, CardEntety> getAllCard() {
        return db;
    }

    @PostMapping("/")
    public CardEntety postCard(@RequestBody CardEntety card) {
        db.put(CardEntety.count + 1, card);
        return db.get(db.size());
    }

    @PutMapping("{id}")
    public CardEntety putCard(@PathVariable Integer id, @RequestBody CardEntety card) {
        db.replace(id, card);
        return db.get(id);
    }

    @DeleteMapping("{id}")
    void deleteCard(@PathVariable Integer id) {
        db.remove(id);
    }

}
