#
# PySNMP MIB module CTRON-ORP-HSIM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-ORP-HSIM-MIB
# Produced by pysmi-1.1.8 at Fri Oct 13 14:02:49 2023
# On host fv-az877-675 platform Linux version 6.2.0-1012-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ctOrpHSIM, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctOrpHSIM")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Counter64, Bits, ModuleIdentity, Counter32, ObjectIdentity, NotificationType, Unsigned32, IpAddress, Integer32, TimeTicks, Gauge32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter64", "Bits", "ModuleIdentity", "Counter32", "ObjectIdentity", "NotificationType", "Unsigned32", "IpAddress", "Integer32", "TimeTicks", "Gauge32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class MacAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

ctOrpHSIMTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 15, 1), )
if mibBuilder.loadTexts: ctOrpHSIMTable.setStatus('mandatory')
ctOrpHSIMEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 15, 1, 1), ).setIndexNames((0, "CTRON-ORP-HSIM-MIB", "ctOrpHSIMSlot"), (0, "CTRON-ORP-HSIM-MIB", "ctOrpHSIMIndex"))
if mibBuilder.loadTexts: ctOrpHSIMEntry.setStatus('mandatory')
ctOrpHSIMSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 15, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctOrpHSIMSlot.setStatus('mandatory')
ctOrpHSIMIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 15, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctOrpHSIMIndex.setStatus('mandatory')
ctOrpHSIMIfRef = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 15, 1, 1, 3), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctOrpHSIMIfRef.setStatus('mandatory')
ctOrpHSIMMACAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 15, 1, 1, 4), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctOrpHSIMMACAddress.setStatus('mandatory')
ctOrpHSIMIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 15, 1, 1, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctOrpHSIMIPAddress.setStatus('mandatory')
ctOrpHSIMSubnetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 15, 1, 1, 6), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctOrpHSIMSubnetMask.setStatus('mandatory')
ctOrpHSIMROCommName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 15, 1, 1, 7), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctOrpHSIMROCommName.setStatus('mandatory')
ctOrpHSIMRWCommName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 15, 1, 1, 8), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctOrpHSIMRWCommName.setStatus('mandatory')
ctOrpHSIMSUCommName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 15, 1, 1, 9), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctOrpHSIMSUCommName.setStatus('mandatory')
mibBuilder.exportSymbols("CTRON-ORP-HSIM-MIB", ctOrpHSIMMACAddress=ctOrpHSIMMACAddress, ctOrpHSIMEntry=ctOrpHSIMEntry, ctOrpHSIMSUCommName=ctOrpHSIMSUCommName, ctOrpHSIMIfRef=ctOrpHSIMIfRef, ctOrpHSIMSlot=ctOrpHSIMSlot, MacAddress=MacAddress, ctOrpHSIMROCommName=ctOrpHSIMROCommName, ctOrpHSIMTable=ctOrpHSIMTable, ctOrpHSIMIndex=ctOrpHSIMIndex, ctOrpHSIMRWCommName=ctOrpHSIMRWCommName, ctOrpHSIMIPAddress=ctOrpHSIMIPAddress, ctOrpHSIMSubnetMask=ctOrpHSIMSubnetMask)
