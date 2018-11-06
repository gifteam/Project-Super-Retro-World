using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class LaserBehavior : MonoBehaviour {

    public GameObject associatedFilter;
    public GameObject associatedTarget;
    public BoxCollider2D targetHitbox;
    public BoxCollider2D hitbox;
    public Vector2 posz;
    public float stepXz;
    public float stepMinXz = 46.0f;
    public float stepMaxXz = 51.0f;

    public float rangeXz;

    // Use this for initialization
    void Start()
    {
        associatedFilter = GameObject.FindGameObjectWithTag("YellowFilter");
        associatedTarget = GameObject.FindGameObjectWithTag("Player");
        targetHitbox = associatedTarget.GetComponent<BoxCollider2D>();
        hitbox = GetComponent<BoxCollider2D>();
        
        posz = new Vector2(0.0f, 0.0f);
        posz = getPos();
        stepXz = 0.02f;
    }

    // Update is called once per frame
    void Update () {

        posz.x += stepXz;
        if (posz.x >= stepMaxXz || posz.x <= stepMinXz)
        {
            stepXz = -1 * stepXz;
        }
        transform.position = posz;


        Vector2 targetPos = associatedTarget.transform.position;
        if (associatedFilter.GetComponent<BoxCollider2D>().bounds.Contains(targetPos))
        {
            Physics2D.IgnoreCollision(targetHitbox, hitbox, true);
        }
        else
        {
            Physics2D.IgnoreCollision(targetHitbox, hitbox, false);
        }


    }

    Vector2 getPos()
    {
        Vector2 pos = transform.position;
        //pos.x -= transform.localScale.x / 2;
        //pos.y -= transform.localScale.y / 2;
        return pos;
    }

}
