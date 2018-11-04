using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class GreenFilterBehavior : MonoBehaviour {

    public BoxCollider2D targetHitbox;
    public BoxCollider2D hitbox;

    // Use this for initialization
    void Start () {
        targetHitbox = GameObject.Find("Player").GetComponent<BoxCollider2D>();
        hitbox = GetComponent<BoxCollider2D>();
        Physics2D.IgnoreCollision(targetHitbox, hitbox, true);
	}
	
	// Update is called once per frame
	void Update () {
		
	}
}
