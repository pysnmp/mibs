#
# PySNMP MIB module EATON-OIDS (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/eaton/EATON-OIDS
# Produced by pysmi-1.1.12 at Tue Dec  3 12:14:46 2024
# On host fv-az573-178 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Integer32, Counter32, iso, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, IpAddress, Counter64, Gauge32, Bits, enterprises, ModuleIdentity, TimeTicks, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Integer32", "Counter32", "iso", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "IpAddress", "Counter64", "Gauge32", "Bits", "enterprises", "ModuleIdentity", "TimeTicks", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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

mibBuilder.exportSymbols("EATON-OIDS", powerwareNetworkSnmpAdapterEther=powerwareNetworkSnmpAdapterEther, eatonPowerXpertMeter=eatonPowerXpertMeter, environmentalMonitor=environmentalMonitor, NonNegativeInteger=NonNegativeInteger, xupsMIB=xupsMIB, powerwareNetworkSnmpAdapterToken=powerwareNetworkSnmpAdapterToken, eatonPdu=eatonPdu, connectUPSAdapterEthernet=connectUPSAdapterEthernet, sts=sts, pduAgent=pduAgent, onlinetDaemon=onlinetDaemon, powerwareEthernetSnmpAdapter=powerwareEthernetSnmpAdapter, itProjects=itProjects, PYSNMP_MODULE_ID=eaton, eatonPowerChainGateway=eatonPowerChainGateway, powerwareEliSnmpAdapter=powerwareEliSnmpAdapter, hdpdu=hdpdu, products=products, dataCenter=dataCenter, powerCmnd=powerCmnd, PositiveInteger=PositiveInteger, powerVision=powerVision, eaton=eaton, powerwareNetworkDigitalIOEther=powerwareNetworkDigitalIOEther, sensorAgent=sensorAgent, xupsObjectId=xupsObjectId, powerwareBasicEmbeddedEthernet=powerwareBasicEmbeddedEthernet, pki=pki, xupsIoMIB=xupsIoMIB, xupsEnvironment=xupsEnvironment, eatonPowerChainDevice=eatonPowerChainDevice, connectUPSAdapterTokenRing=connectUPSAdapterTokenRing, powerChain=powerChain, simpleSnmpAdapter=simpleSnmpAdapter)
