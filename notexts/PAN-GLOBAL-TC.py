#
# PySNMP MIB module PAN-GLOBAL-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/paloaltonetworks/PAN-GLOBAL-TC-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 17:16:21 2022
# On host fv-az135-792 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
panModules, = mibBuilder.importSymbols("PAN-GLOBAL-REG", "panModules")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Gauge32, Integer32, ModuleIdentity, MibIdentifier, NotificationType, Counter32, Unsigned32, Counter64, IpAddress, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Gauge32", "Integer32", "ModuleIdentity", "MibIdentifier", "NotificationType", "Counter32", "Unsigned32", "Counter64", "IpAddress", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
panGlobalTcModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 25461, 1, 1, 2))
panGlobalTcModule.setRevisions(('2011-02-09 16:10',))
if mibBuilder.loadTexts: panGlobalTcModule.setLastUpdated('201106271040Z')
if mibBuilder.loadTexts: panGlobalTcModule.setOrganization('Palo Alto Networks')
class TcAppaname(TextualConvention, OctetString):
    status = 'current'
    displayHint = '64a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class TcChassisType(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

mibBuilder.exportSymbols("PAN-GLOBAL-TC", PYSNMP_MODULE_ID=panGlobalTcModule, panGlobalTcModule=panGlobalTcModule, TcAppaname=TcAppaname, TcChassisType=TcChassisType)
