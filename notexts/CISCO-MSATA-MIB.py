#
# PySNMP MIB module CISCO-MSATA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-MSATA-MIB
# Source digest sha256:5ba338aa28e11000ac223cd97e3bb8150fd9bd116674395eb2a85b2a32abdfdf
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoMsataMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 860))
ciscoMsataMIB.setRevisions(('2019-01-09 00:00',))
if mibBuilder.loadTexts: ciscoMsataMIB.setLastUpdated('2019-01-09 00:00')
if mibBuilder.loadTexts: ciscoMsataMIB.setOrganization('Cisco Systems, Inc.')
ciscoMsataMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 860, 0))
ciscoMsata = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 860, 0, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoMsata.setStatus('current')
mibBuilder.exportSymbols("CISCO-MSATA-MIB", PYSNMP_MODULE_ID=ciscoMsataMIB, ciscoMsata=ciscoMsata, ciscoMsataMIB=ciscoMsataMIB, ciscoMsataMIBObjects=ciscoMsataMIBObjects)
