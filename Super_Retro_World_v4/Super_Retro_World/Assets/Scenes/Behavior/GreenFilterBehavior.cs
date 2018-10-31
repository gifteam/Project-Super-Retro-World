using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class GreenFilterBehavior : MonoBehaviour {

    public BoxCollider2D charHitbox;
    public BoxCollider2D hitbox;

    // Use this for initialization
    void Start () {
        charHitbox = GameObject.Find("Character").GetComponent<BoxCollider2D>();
        hitbox = GetComponent<BoxCollider2D>();
        Physics2D.IgnoreCollision(charHitbox, hitbox, true);
	}
	
	// Update is called once per frame
	void Update () {
		
	}
}
