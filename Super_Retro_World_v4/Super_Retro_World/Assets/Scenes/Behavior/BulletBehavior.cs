using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class BulletBehavior : MonoBehaviour {

    public GameObject target;
    public GameObject[] greenFilters;
    public bool hasShot;
    public Vector2 deltaPos;

    // Use this for initialization
    void Start () {
        deltaPos = new Vector2(0.0f, 0.0f);
        hasShot = false;
        greenFilters = GameObject.FindGameObjectsWithTag("GreenFilter");
    }
	
	// Update is called once per frame
	void Update () {
		if (hasShot)
        {
            deltaPos.x = (target.transform.position.x - transform.position.x) / 100;
            deltaPos.y = (target.transform.position.y - transform.position.y) / 100;
            hasShot = false;
        }

        if (deltaPos.x != 0 || deltaPos.y != 0)
        {
            Vector2 pos = getPos();
            pos += deltaPos;
            transform.position = pos;

            gameObject.GetComponent<BoxCollider2D>().size = new Vector2(1, 1);
            foreach (GameObject gF in greenFilters)
            {
                BoxCollider2D greenFilterHitbox;
                greenFilterHitbox = gF.GetComponent<BoxCollider2D>();
                if (greenFilterHitbox.bounds.Contains(pos))
                {
                    gameObject.GetComponent<BoxCollider2D>().size = new Vector2(0, 0);
                    break;
                }
            }
        }
    }

    public void setTarget(GameObject target_)
    {
        target = target_;
    }

    public void load(Vector2 pos)
    {
        setPos(pos);
    }

    void setPos(Vector2 pos)
    {
        transform.position = pos;
    }

    public void shoot()
    {
        hasShot = true;
    }

    Vector2 getPos()
    {
        return transform.position;
    }
}
