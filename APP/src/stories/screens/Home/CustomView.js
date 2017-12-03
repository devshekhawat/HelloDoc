import PropTypes from 'prop-types';
import React from 'react';
import {
  Linking,
  Platform,
  StyleSheet,
  Text,
  ViewPropTypes,
} from 'react-native';

export default class CustomView extends React.Component {
  render() {
    if (this.props.currentMessage.location) {
      return (
        <Text>
		DEV
        </Text>
      );
    }
    return null;
  }
}

const styles = StyleSheet.create({
  container: {
  },
  mapView: {
    width: 150,
    height: 100,
    borderRadius: 13,
    margin: 3,
  },
});

CustomView.defaultProps = {
  currentMessage: {},
  containerStyle: {},
  mapViewStyle: {},
};

CustomView.propTypes = {
  currentMessage: PropTypes.object,
  containerStyle: ViewPropTypes.style,
  mapViewStyle: ViewPropTypes.style,
};