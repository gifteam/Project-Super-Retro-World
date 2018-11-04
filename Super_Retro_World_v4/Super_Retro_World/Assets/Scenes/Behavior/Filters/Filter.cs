using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Filter : MonoBehaviour
{
    // =============================================================================
    // A filter is an rectangle object hidding plateform outside of its bounds
    // The filter has one specific color and came from a fake light source
    //
    //     +----------------------+
    //     |                      | 
    //     |                      | 
    //     |                      | 
    //     |                      | 
    //     |                      | 
    //     +----------------------+
    //       <== Filter object ==>
    //
    //
    //           \         /
    //            \       /
    //             \     /
    //                X
    //          Light source
    //
    //
    // The filter will go left and right with a smooth speed transition
    // =============================================================================

    // =============================================================================
    // Class variable
    // =============================================================================

    // -----------------------------------------------------------------------------
    // positions variables
    public Vector2 pos;
    public float stepX;
    // min and max X bounds (will start to smoothly brake there)
    public float stepMinX = -3.0f;
    public float stepMaxX =  3.0f;
    // -----------------------------------------------------------------------------
    // GO component variables
    private GO go;
    public string tag;
    public Rigidbody2D body;
    // -----------------------------------------------------------------------------
    // Effets (children)
    public Transform rays;
    public Transform sides;
    public Transform corners;

    // =============================================================================
    // Use this for initialization
    // =============================================================================
    void Start ()
    {
        // set GO instance
        this.go = new GO(gameObject);
        tag = gameObject.tag;
        // current position of the Mask part (this GO)
        pos = new Vector2(0.0f, 0.0f);
        pos = go.posCen();
        // step in X direction set
        stepX = 0.02f;
        // find children by looping through every one of them
        foreach (Transform child in transform.parent)
        {
            switch (child.gameObject.name)
            {
                case "Rays":
                    rays = child;
                    break;
                case "Sides":
                    sides = child;
                    break;
                case "Corners":
                    corners = child;
                    break;
            }
        }
    }
    // =============================================================================
    // Update is called once per frame
    // =============================================================================
    void Update() {

        if (tag == "RedFilter")
        {
            pos.x += stepX;
            if (pos.x >= stepMaxX || pos.x <= stepMinX)
            {
                stepX = -1 * stepX;
            }
            transform.position = pos;

            updateRays();
            updateSides();
            updateCorners();
        }
    }
    // =============================================================================
    // Update effects (rays, sides and corners positions)
    // =============================================================================
    void updateRays()
    {
        foreach (Transform ray in rays)
        {
            Transform line = ray;
            LineRenderer lineRenderer = line.GetComponent<LineRenderer>();
            Vector2 point = new Vector2(0.0f, 0.0f);

            switch (line.gameObject.name)
            {
                case "TopLeft":
                    point = go.posTopLeft();
                    break;
                case "TopRight":
                    point = go.posTopRight();
                    break;
                case "BotLeft":
                    point = go.posBotLeft();
                    break;
                case "BotRight":
                    point = go.posBotRight();
                    break;
            }
            lineRenderer.SetPosition(0, new Vector3(0.0f, -1.0f, 0.0f));
            lineRenderer.SetPosition(1, new Vector3(point.x / 2.0f, (point.y - 1.0f) / 2.0f, 0.0f));
            lineRenderer.SetPosition(2, new Vector3(point.x, point.y, 0.0f));
        }
    }
    void updateSides()
    {
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
            lineRenderer.SetPosition(0, new Vector3(point0.x, point0.y, 0.0f));
            lineRenderer.SetPosition(1, new Vector3(point1.x, point1.y, 0.0f));
        }
    }
    void updateCorners() { 

        foreach (Transform corner in corners)
        {
            Vector2 point = new Vector2(0.0f, 0.0f);
            switch (corner.gameObject.name)
            {
                case "TopLeft":
                    point = go.posTopLeft();
                    break;
                case "TopRight":
                    point = go.posTopRight();
                    break;
                case "BotLeft":
                    point = go.posBotLeft();
                    break;
                case "BotRight":
                    point = go.posBotRight();
                    break;
            }
            corner.position = point;
        }
    }
}
