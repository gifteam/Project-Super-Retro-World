using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class RedPlateformBehavior : MonoBehaviour {

    public BoxCollider2D hitbox;
    public GameObject filter;

    // Use this for initialization
    void Start() {
        filter = getNewFilter("RedFilter");
        hitbox = gameObject.GetComponent<BoxCollider2D>();
        //get mask sprite

    }

    // Update is called once per frame
    void Update() {

        setHitSizeW(1.0f);

        //get self size (width)
        float Pw = getWidth();
        //get self position (topleft X)
        Vector2 Ppos = getPos();
        //get mask size (width)
        float Fw = getFilterWidth();
        //get mask position (topleft X)
        Vector2 Fpos = getFilterPos();

        //collider offset X update (0 to 100%)
        float offX = 0.0f; //start at 0% by default
        float sizeW = 1.0f; // start at 100% by default

        if (Ppos.x + Pw < Fpos.x || Ppos.x > Fpos.x + Fw) // completely outside the filter
        {
            offX = 0.0f;
            sizeW = 0.0f;
        }
        else if (Ppos.x < Fpos.x && Ppos.x + Pw >= Fpos.x)
        {
            sizeW = 1.0f - ( (Fpos.x - Ppos.x) / Pw );
            offX = 0.5f - (sizeW) / 2.0f;
        }
        else if (Ppos.x >= Fpos.x && Ppos.x + Pw <= Fpos.x + Fw)
        {
            sizeW = 1.0f;
            offX = 0.0f;
        }
        else if ( (Ppos.x <= Fpos.x + Fw) && (Ppos.x + Pw > Fpos.x + Fw) )
        {
            sizeW = (Fpos.x + Fw - Ppos.x) / Pw;
            offX = -0.5f + (sizeW) / 2.0f;
        }
        setHitOffX(offX);
        setHitSizeWidth(sizeW);
    }

    void setHitOffX(float offX)
    {
        float offY = hitbox.offset.y;
        hitbox.offset = new Vector2(offX, offY);
    }

    void setHitSizeWidth(float w)
    {
        hitbox.size = new Vector2(w, 1);
    }

    float getWidth()
    {
        return transform.localScale.x;
    }

    Vector2 getPos()
    {
        Vector2 pos = transform.position;
        pos.x -= transform.localScale.x / 2;
        pos.y -= transform.localScale.y / 2;
        return pos;
    }

    void setHitSizeW(float sizeW)
    {
        float sizeH = hitbox.size.y;

        hitbox.size = new Vector2(sizeW, sizeH);
    }

    GameObject getNewFilter(string tag)
    {
        return GameObject.FindGameObjectWithTag(tag);
    }

    Vector2 getFilterPos()
    {
        Vector2 pos = filter.transform.position;
        pos.x -= filter.transform.localScale.x / 2;
        pos.y -= filter.transform.localScale.y / 2;
        return pos;
    }

    float getFilterWidth()
    {
        float scaleW = filter.transform.localScale.x;
        return scaleW;
    }

    float getFilterHeight()
    {
        float scaleH = filter.transform.localScale.y;
        return scaleH;
    }
}
