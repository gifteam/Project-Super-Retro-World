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
    public Transform parent;
    public Transform rays;
    public Transform sides;
    public Transform corners;
    private GO go;

    // Use this for initialization
    void Start ()
    {
        this.go = new GO(gameObject);
        filterTag = gameObject.tag;
        pos = new Vector2(0.0f, 0.0f);
        pos = getPos();
        stepX = 0.02f;
        parent = transform.parent;
        foreach (Transform child in parent)
        {
            if (child.gameObject.name == "Rays")
            {
                rays = child;
            }
            if (child.gameObject.name == "Sides")
            {
                sides = child;
            }
            if (child.gameObject.name == "Corners")
            {
                corners = child;
            }
        }

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


            foreach (Transform ray in rays)
            {
                Transform line = ray;
                LineRenderer lineRenderer = line.GetComponent<LineRenderer>();
                Vector2 corner = new Vector2(0.0f, 0.0f);

                switch (line.gameObject.name)
                {
                    case "TopLeft":
                        corner = go.posTopLeft();
                        break;
                    case "TopRight":
                        corner = go.posTopRight();
                        break;
                    case "BotLeft":
                        corner = go.posBotLeft();
                        break;
                    case "BotRight":
                        corner = go.posBotRight();
                        break;
                }
                lineRenderer.SetPosition(0, new Vector3(0.0f, -1.0f, 0.0f));
                lineRenderer.SetPosition(1, new Vector3(corner.x/2.0f, (corner.y-1.0f) / 2.0f, 0.0f));
                lineRenderer.SetPosition(2, new Vector3(corner.x, corner.y, 0.0f));
            }

            foreach (Transform side in sides)
            {
                Transform line = side;
                LineRenderer lineRenderer = line.GetComponent<LineRenderer>();
                Vector2 point0 = new Vector2(0.0f, 0.0f);
                Vector2 point1 = new Vector2(0.0f, 0.0f);

                switch (line.gameObject.name)
                {
                    case "Left":
                        point0 = go.posBotLeft();
                        point1 = go.posTopLeft();
                        break;
                    case "Right":
                        point0 = go.posBotRight();
                        point1 = go.posTopRight();
                        break;
                    case "Top":
                        point0 = go.posTopLeft();
                        point1 = go.posTopRight();
                        break;
                    case "Bot":
                        point0 = go.posBotLeft();
                        point1 = go.posBotRight();
                        break;
                }
                lineRenderer.SetPosition(0, new Vector3 (point0.x, point0.y, 0.0f));
                lineRenderer.SetPosition(1, new Vector3 (point1.x, point1.y, 0.0f));
            }

            foreach (Transform corn in corners)
            {
                Vector2 cornerPos = new Vector2(0.0f, 0.0f);
                switch (corn.gameObject.name)
                {
                    case "TopLeft":
                        cornerPos = go.posTopLeft();
                        break;
                    case "TopRight":
                        cornerPos = go.posTopRight();
                        break;
                    case "BotLeft":
                        cornerPos = go.posBotLeft();
                        break;
                    case "BotRight":
                        cornerPos = go.posBotRight();
                        break;
                }
                corn.position = cornerPos;
            }
        }
    }

    Vector2 getPos()
    {
        return transform.position;
    }
}
