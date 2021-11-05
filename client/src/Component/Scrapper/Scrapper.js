import React from "react";
import Styled from 'styled-components';

const ScrapSidebar = Styled.div`
position: fixed;
width: 120px;
height: 400px;
margin-left : auto;
margin-right : auto;
`

const InputUrl = Styled.form`
width: 100px;
height: 55px;
`

const Output = Styled.div`
width : 50%;

`

export default function Scrapper() {
    return (
        <ScrapSidebar>
            <InputUrl  methods={['GET']}>
                <input type="url" name="url" placeholder="plz input url" />
                <button type="submit">enter</button>
            </InputUrl>
            <Output />
        </ ScrapSidebar>
    )
}