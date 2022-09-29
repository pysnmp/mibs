#
# PySNMP MIB module EATON-OIDS (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/eaton/EATON-OIDS
# Produced by pysmi-1.1.8 at Thu Sep 29 13:08:28 2022
# On host fv-az359-613 platform Linux version 5.15.0-1020-azure by user runner
# Using Python version 3.10.7 (main, Sep  6 2022, 15:19:58) [GCC 9.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, iso, enterprises, Integer32, Bits, TimeTicks, Gauge32, NotificationType, ObjectIdentity, IpAddress, Counter32, MibIdentifier, ModuleIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "iso", "enterprises", "Integer32", "Bits", "TimeTicks", "Gauge32", "NotificationType", "ObjectIdentity", "IpAddress", "Counter32", "MibIdentifier", "ModuleIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
eaton = ModuleIdentity((1, 3, 6, 1, 4, 1, 534))
eaton.setRevisions(('2018-11-13 00:00', '2014-02-19 00:00', '2010-01-24 00:00', '2009-06-18 00:00', '2007-08-06 00:00', '2007-07-05 00:00', '2006-10-15 00:00', '2006-05-25 00:00',))
if mibBuilder.loadTexts: eaton.setLastUpdated('201811130000Z')
if mibBuilder.loadTexts: eaton.setOrganization('Eaton Corporation')
xupsMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 1))
xupsEnvironment = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 1, 6))
xupsObjectId = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 2))
powerwareEthernetSnmpAdapter = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 2, 1))
powerwareNetworkSnmpAdapterEther = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 2, 2))
powerwareNetworkSnmpAdapterToken = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 2, 3))
onlinetDaemon = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 2, 4))
connectUPSAdapterEthernet = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 2, 5))
powerwareNetworkDigitalIOEther = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 2, 6))
connectUPSAdapterTokenRing = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 2, 7))
simpleSnmpAdapter = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 2, 8))
powerwareEliSnmpAdapter = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 2, 9))
powerwareBasicEmbeddedEthernet = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 2, 10))
eatonPowerChainGateway = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 2, 11))
eatonPowerChainDevice = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 2, 12))
eatonPowerXpertMeter = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 2, 13))
xupsIoMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 3))
powerVision = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 4))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 6))
pduAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 6, 6))
hdpdu = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 6, 6, 2))
eatonPdu = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 6, 6, 4))
sensorAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 6, 8))
dataCenter = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 6, 7))
environmentalMonitor = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 6, 7, 1))
itProjects = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 7))
pki = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 7, 1))
powerChain = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 8))
powerCmnd = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 9))
sts = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 10))
class PositiveInteger(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class NonNegativeInteger(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

mibBuilder.exportSymbols("EATON-OIDS", PositiveInteger=PositiveInteger, eatonPowerXpertMeter=eatonPowerXpertMeter, powerwareBasicEmbeddedEthernet=powerwareBasicEmbeddedEthernet, hdpdu=hdpdu, eaton=eaton, xupsObjectId=xupsObjectId, connectUPSAdapterEthernet=connectUPSAdapterEthernet, powerwareNetworkSnmpAdapterToken=powerwareNetworkSnmpAdapterToken, xupsMIB=xupsMIB, eatonPdu=eatonPdu, sts=sts, onlinetDaemon=onlinetDaemon, powerwareNetworkDigitalIOEther=powerwareNetworkDigitalIOEther, powerwareEliSnmpAdapter=powerwareEliSnmpAdapter, connectUPSAdapterTokenRing=connectUPSAdapterTokenRing, eatonPowerChainGateway=eatonPowerChainGateway, powerwareNetworkSnmpAdapterEther=powerwareNetworkSnmpAdapterEther, environmentalMonitor=environmentalMonitor, itProjects=itProjects, PYSNMP_MODULE_ID=eaton, dataCenter=dataCenter, simpleSnmpAdapter=simpleSnmpAdapter, eatonPowerChainDevice=eatonPowerChainDevice, powerwareEthernetSnmpAdapter=powerwareEthernetSnmpAdapter, products=products, xupsIoMIB=xupsIoMIB, sensorAgent=sensorAgent, powerChain=powerChain, pduAgent=pduAgent, NonNegativeInteger=NonNegativeInteger, xupsEnvironment=xupsEnvironment, powerCmnd=powerCmnd, powerVision=powerVision, pki=pki)
