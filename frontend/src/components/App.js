import React from 'react'
import styled from 'styled-components'
import GridRow from '@govuk-react/grid-row'
import GridCol from '@govuk-react/grid-col'

import Main from '@govuk-react/main'

import PageHeader from './PageHeader'
import PhaseBanner from '@govuk-react/phase-banner'
import Footer from '@govuk-react/footer'
import Paragraph from '@govuk-react/paragraph'
import { H1 } from '@govuk-react/heading'
import Button from '@govuk-react/button'
import { ButtonArrow } from '@govuk-react/icons'

const MyMain = styled(Main)`
  padding-top: 0;
`

const App = () => {
  return (
    <div>
      <PageHeader />
      <MyMain>
        <GridRow>
          <GridCol>
            <PhaseBanner level="alpha">
              This is an initial implementation of Statement of Works.
            </PhaseBanner>
          </GridCol>
        </GridRow>
        <GridRow>
          <GridCol>
            <br />
            <H1>Create Statement of Works document</H1>
            <Paragraph>
              Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi
              lacinia at velit eget dapibus. Cras mollis lorem eros, a lacinia
              metus bibendum et. Proin egestas, turpis nec ultricies suscipit,
              odio arcu porta mauris, sit amet lobortis diam libero eget odio.
              Donec lacus purus, suscipit eu nunc eu, ultricies iaculis massa.
              Etiam sodales lacus et interdum semper. Sed eleifend fermentum
              ligula, vel scelerisque ex pellentesque et. Pellentesque et tortor
              euismod, tincidunt tellus sit amet, varius massa. Morbi
              sollicitudin varius augue nec blandit. Mauris posuere in ante quis
              egestas. Nulla pellentesque egestas neque vel facilisis. Donec
              felis ipsum, malesuada vitae neque eu, fermentum molestie urna.
              Fusce eget lacus bibendum, vehicula nisl vel, aliquet nisi.
            </Paragraph>
            <Button icon={<ButtonArrow />}>Start now</Button>
          </GridCol>
        </GridRow>
      </MyMain>
      <Footer />
    </div>
  )
}

export default App
