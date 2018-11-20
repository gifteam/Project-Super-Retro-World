using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Perceptron
{
    //public float m_weigth;
    public float m_value;
    public List<PerceptronInput> m_inputList;
    public List<PerceptronOutput> m_outputList;
    public BlocPop m_blocPop;
    public Control m_control;

    public Perceptron(BlocPop a_blocPop, Control a_control)
    {
        m_control = a_control;
        m_blocPop = a_blocPop;
        m_inputList = new List<PerceptronInput>();
        m_outputList = new List<PerceptronOutput>();

        //m_weigth = Random.Range(-1.0f, 1.0f);

        int l_inputs = m_blocPop.m_nbBloc; // (uint)Mathf.RoundToInt(Random.Range(0.0f, 3.0f));
        for (int i_inputIndex = 0; i_inputIndex < l_inputs; i_inputIndex++)
        {
            m_inputList.Add(new PerceptronInput(m_blocPop, i_inputIndex));
        }

        int l_outputs = m_control.m_keys.Count;
        for (int i_outputIndex = 0; i_outputIndex < l_outputs; i_outputIndex++)
        {
            m_outputList.Add(new PerceptronOutput(m_control, i_outputIndex));
        }
    }

    public void update()
    {
        m_value = 0;
        foreach (PerceptronInput i in m_inputList)
        {
            i.update();
            m_value += i.m_value;
        }
        //m_value += m_weigth;

        if (m_value > 1f)
        {
            m_value = 1f;
        }
        else if (m_value < -1f)
        {
            m_value = -1f;
        }

        foreach (PerceptronOutput o in m_outputList)
        {
            o.update(m_value);
        }
    }

    public void showInputWeight()
    {
        string l_listValues = "";
        foreach (PerceptronInput i in m_inputList)
        {
            l_listValues += i.m_weigth + ";";
        }
        Debug.Log(l_listValues);
    }
}

public class PerceptronInput
{
    public int m_blocIndex;
    public float m_weigth;
    public float m_value;
    public BlocPop m_blocPop;

    public PerceptronInput(BlocPop a_blocPop, int a_blocIndex)
    {
        m_blocPop = a_blocPop;
        m_blocIndex = a_blocIndex; // Mathf.RoundToInt(Random.Range(0.0f, m_blocPop.m_nbBloc - 1f));
        m_weigth = Random.Range(-1.0f, 1.0f);
        m_value = 0;
    }

    public void update()
    {
        m_value = m_blocPop.m_BlocList[m_blocIndex].m_value * m_weigth;
    }
}

public class PerceptronOutput
{
    public int m_keyIndex;
    public float m_weigth;
    public float m_value;
    public Control m_control;

    public PerceptronOutput(Control a_control, int a_keyIndex)
    {
        m_control = a_control;
        m_keyIndex = a_keyIndex; // Mathf.RoundToInt(Random.Range(0.0f, m_control.m_keys.Count - 1f));
        m_weigth = Random.Range(-1.0f, 1.0f);
    }

    public void update(float a_value)
    {
        m_value = a_value * m_weigth;
        m_control.m_keys[m_keyIndex] += m_value;
    }
}
