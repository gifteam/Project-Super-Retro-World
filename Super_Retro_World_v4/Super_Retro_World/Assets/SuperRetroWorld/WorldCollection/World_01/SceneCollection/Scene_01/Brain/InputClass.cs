using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class BlocPop
{
    public int m_nbBlocX;
    public int m_nbBloxY;
    public int m_nbBloc;
    public GO m_target;
    public GO m_blocOriginal;

    public List<Bloc> m_BlocList;

    public BlocPop(GO a_target)
    {
        m_target = a_target;
        m_nbBlocX = 4;
        m_nbBloxY = 4;
        m_nbBloc = m_nbBlocX * m_nbBloxY;
        m_blocOriginal = new GO(GameObject.Find("InputBloc"));


        m_BlocList = new List<Bloc>();

        for (int i_blocIndex = 0; i_blocIndex < m_nbBloc; i_blocIndex++)
        {
            float l_sclX = m_blocOriginal.getGO().transform.localScale.x;
            float l_sclY = m_blocOriginal.getGO().transform.localScale.y;
            float l_deltaX = ( ( i_blocIndex % m_nbBlocX ) - ( m_nbBlocX / 2f ) ) * l_sclX;
            float l_deltaY = ( ( i_blocIndex / m_nbBlocX ) - ( m_nbBlocX / 2f ) ) * l_sclY;
            m_BlocList.Add(new Bloc(m_target, l_deltaX, l_deltaY));
        }
    }

    public void update()
    {
        foreach (Bloc b in m_BlocList)
        {
            b.update();
        }
    }
}

public class Bloc
{
    public int m_value;
    public GO m_go;
    public GO m_goOrigin;
    public GO m_parent;

    public Bloc(GO a_parent, float a_deltaX, float a_deltaY)
    {
        m_parent = a_parent;
        m_goOrigin = new GO(GameObject.Find("InputBloc"));
        m_go = new GO(GameObject.Instantiate(m_goOrigin.getGO().transform, m_parent.getGO().transform).gameObject);
        Vector2 l_blocPos = new Vector2(a_deltaX, a_deltaY);
        m_go.setLocalPos(l_blocPos);
        m_value = 0;
    }

    public void update()
    {
        Rect l_blocRect = m_go.getBoxCollider2DRect();
        m_value = 0;
        foreach(GameObject l_go in GameObject.FindGameObjectsWithTag("Platform"))
        {
            if (l_blocRect.Overlaps(new GO(l_go).getBoxCollider2DRect()))
            {
                m_value = 1;
                break;
            }
        }

        if (m_value == 0)
        {
            GameObject l_player = GameObject.FindGameObjectWithTag("Player");
            if (l_blocRect.Overlaps(new GO(l_player).getBoxCollider2DRect()))
            {
                m_value = -1;
            }
        }

        Color l_color;
        switch (m_value)
        {
            case 1:
                l_color = Color.blue;
                break;
            case -1:
                l_color = Color.red;
                break;
            default:
                l_color = Color.green;
                break;
        }
        SpriteRenderer l_SpriteRenderer = m_go.getGO().GetComponent<SpriteRenderer>();
        l_SpriteRenderer.color = l_color;
    }


}