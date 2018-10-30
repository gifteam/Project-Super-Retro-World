using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class FilterBehavior : MonoBehaviour {

    public Vector2 pos;
    public float stepX;
    public Rigidbody2D body;

    // Use this for initialization
    void Start ()
    {
        pos = new Vector2(0.0f, 0.0f);
        pos = getPos();
        stepX = -0.02f;
	}
	
	// Update is called once per frame
	void Update () {
        pos.x += stepX;

        if (pos.x >= 7 || pos.x <= -3){
            stepX = -1 * stepX;
        }

        transform.position = pos;
	}

    Vector2 getPos()
    {
        return transform.position;
    }
}
