using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class FilterBehavior : MonoBehaviour {

    public Vector2 pos;
    public float stepX;
    public float stepMinX = -2.0f;
    public float stepMaxX = 5.0f;
    public Rigidbody2D body;
    public string filterTag;

    // Use this for initialization
    void Start ()
    {
        filterTag = gameObject.tag;
        pos = new Vector2(0.0f, 0.0f);
        pos = getPos();
        stepX = 0.02f;
    }
	
	// Update is called once per frame
	void Update () {

        if (filterTag == "RedFilter")
        {
            pos.x += stepX;
            if (pos.x >= stepMaxX || pos.x <= stepMinX)
            {
                stepX = -1 * stepX;
            }
            transform.position = pos;
        }
    }

    Vector2 getPos()
    {
        return transform.position;
    }
}
