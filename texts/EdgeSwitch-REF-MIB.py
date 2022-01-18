#
# PySNMP MIB module EdgeSwitch-REF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/edgeswitch/EdgeSwitch-REF-MIB
# Produced by pysmi-1.1.8 at Tue Jan 18 14:47:17 2022
# On host fv-az39-968 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, iso, IpAddress, TimeTicks, Unsigned32, MibIdentifier, Counter64, ModuleIdentity, Bits, Integer32, Counter32, ObjectIdentity, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "iso", "IpAddress", "TimeTicks", "Unsigned32", "MibIdentifier", "Counter64", "ModuleIdentity", "Bits", "Integer32", "Counter32", "ObjectIdentity", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
broadcom = ModuleIdentity((1, 3, 6, 1, 4, 1, 4413))
broadcom.setRevisions(('2007-05-23 00:00', '2003-11-21 00:00', '2003-02-06 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: broadcom.setRevisionsDescriptions(('Ubiquiti branding related changes.', 'Revisions made for new release.', 'Updated for release',))
if mibBuilder.loadTexts: broadcom.setLastUpdated('200705230000Z')
if mibBuilder.loadTexts: broadcom.setOrganization('Broadcom Inc')
if mibBuilder.loadTexts: broadcom.setContactInfo('')
if mibBuilder.loadTexts: broadcom.setDescription('')
broadcomProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1))
fastPath = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 1))
class AgentPortMask(TextualConvention, OctetString):
    description = "Each octet within this value specifies a set of eight\n        ports, with the first octet specifying ports 1 through\n        8, the second octet specifying ports 9 through 16, etc.\n        Within each octet, the most significant bit represents\n        the lowest numbered port, and the least significant bit\n        represents the highest numbered port.  Thus, each port\n        of the bridge is represented by a single bit within the\n        value of this object.  If that bit has a value of '1'\n        then that port is included in the set of ports; the port\n        is not included if its bit has a value of '0'\n             \n        When setting this value, the system will ignore \n        configuration for ports not between the first and last \n        valid ports.  Configuration of any port numbers between \n        this range that are not valid ports return a failure \n        message, but will still apply configuration for valid \n        ports."
    status = 'current'

mibBuilder.exportSymbols("EdgeSwitch-REF-MIB", broadcom=broadcom, AgentPortMask=AgentPortMask, broadcomProducts=broadcomProducts, fastPath=fastPath, PYSNMP_MODULE_ID=broadcom)
