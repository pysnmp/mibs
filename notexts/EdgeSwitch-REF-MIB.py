#
# PySNMP MIB module EdgeSwitch-REF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/edgeswitch/EdgeSwitch-REF-MIB
# Produced by pysmi-1.1.12 at Tue Dec  3 12:14:51 2024
# On host fv-az573-178 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, Integer32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, enterprises, Gauge32, IpAddress, MibIdentifier, TimeTicks, Counter32, ObjectIdentity, Unsigned32, NotificationType, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Integer32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "enterprises", "Gauge32", "IpAddress", "MibIdentifier", "TimeTicks", "Counter32", "ObjectIdentity", "Unsigned32", "NotificationType", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
broadcom = ModuleIdentity((1, 3, 6, 1, 4, 1, 4413))
broadcom.setRevisions(('2007-05-23 00:00', '2003-11-21 00:00', '2003-02-06 12:00',))
if mibBuilder.loadTexts: broadcom.setLastUpdated('200705230000Z')
if mibBuilder.loadTexts: broadcom.setOrganization('Broadcom Inc')
broadcomProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1))
fastPath = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 1))
class AgentPortMask(TextualConvention, OctetString):
    status = 'current'

mibBuilder.exportSymbols("EdgeSwitch-REF-MIB", AgentPortMask=AgentPortMask, PYSNMP_MODULE_ID=broadcom, broadcomProducts=broadcomProducts, broadcom=broadcom, fastPath=fastPath)
